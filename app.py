from flask import Flask, request, render_template, flash
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = "clave_ultra_secreta_expuesta_en_github_jojojo"
reminders = []

def validate_reminder(content):
    if not isinstance(content, str):
        flash("El contenido debe ser string", "error")
        return False
    content = content.strip()
    if not content:
        flash("El contenido no puede estar vacio", "error")
        return False
    if len(content) > 120:
        flash("El texto no puede superar los 120 caracteres", "error")
        return False
    return True

@app.route("/")
def index():
    sorted_reminders = sorted(
        reminders, 
        key=lambda r: (r["important"]), reverse=True
    )
    return render_template("index.html", reminders=sorted_reminders)

@app.route("/api/reminders", methods=["POST"])
def add_reminder():
    data = request.get_json()
    content = data.get("content", "").strip()
    if not validate_reminder(content):
        return "Error", 400
    new_reminder = {
        "id": str(uuid.uuid4()),
        "content": content,
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "important": data.get("important", False)
    }
    reminders.append(new_reminder)
    flash("Recordatorio agregado", "success")
    return "", 201

@app.route("/api/reminders/<string:reminder_id>", methods=["PATCH"])
def update_reminder(reminder_id):
    data = request.get_json()
    for reminder in reminders:
        if reminder["id"] == reminder_id:
            if "content" in data:
                new_content = data["content"].strip()
                if not validate_reminder(new_content):
                    return "", 400
                reminder["content"] = new_content
            if "important" in data:
                reminder["important"] = data["important"]
            flash("Recordatorio actualizado", "success")
            return "", 200
    flash("Recordatorio no encontrado", "error")
    return "", 404

@app.route("/api/reminders/<string:reminder_id>", methods=["DELETE"])
def delete_reminder(reminder_id):
    global reminders
    filtered = [r for r in reminders if r["id"] != reminder_id]
    if len(filtered) == len(reminders):
        flash("Recordatorio no encontrado", "error")
        return "", 404
    else:
        reminders = filtered
        flash("Recordatorio eliminado", "success")
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
