from flask import Flask, jsonify, request
import requests
from config import SUPABASE_URL, SUPABASE_API_KEY

app = Flask(__name__)

HEADERS = {
    "apikey": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxhZ2NzaWl2YnR4dGtoamlyZHF6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM3MDQ0MTMsImV4cCI6MjA1OTI4MDQxM30.POTHZPQO1-7Z8APwoGgXaR8Dw9ZF-WbTREyc5n639pI,
    "Authorization": f"Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxhZ2NzaWl2YnR4dGtoamlyZHF6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM3MDQ0MTMsImV4cCI6MjA1OTI4MDQxM30.POTHZPQO1-7Z8APwoGgXaR8Dw9ZF-WbTREyc5n639pI}",
    "Content-Type": "application/json"
}

# 🟢 جلب كل المشاريع
@app.route('/projects', methods=['GET'])
def get_projects():
    response = requests.get(f"{https://lagcsiivbtxtkhjirdqz.supabase.co}/rest/v1/projects", headers=HEADERS)
    return jsonify(response.json())

# 🟡 إضافة مشروع جديد
@app.route('/projects', methods=['POST'])
def add_project():
    data = request.json
    response = requests.post(f"{https://lagcsiivbtxtkhjirdqz.supabase.co}/rest/v1/projects", headers=HEADERS, json=data)
    return jsonify(response.json())

# 🔵 تحديث مشروع حسب ID
@app.route('/projects/<int:project_id>', methods=['PATCH'])
def update_project(project_id):
    data = request.json
    response = requests.patch(
        f"{https://lagcsiivbtxtkhjirdqz.supabase.co}/rest/v1/projects?id=eq.{project_id}",
        headers=HEADERS,
        json=data
    )
    return jsonify(response.json())

# 🚀 تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
