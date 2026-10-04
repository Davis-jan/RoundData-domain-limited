from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.secret_key = 'change-this-secret-key-in-production'

SERVICES = [
    {
        'number': '01', 'name': 'Training & Capacity Building', 'short': 'Build practical skills that move from the classroom into everyday work.',
        'intro': 'Our core service is structured, practical learning designed for teams, professionals, SMEs, NGOs and freelancers.',
        'items': ['Corporate workshops and programmes', 'Professional team courses', 'Sector-specific training', 'Decision-making and performance', 'Operational efficiency', 'Strategic planning']
    },
    {
        'number': '02', 'name': 'Advisory Services', 'short': 'Turn knowledge and frameworks into practical action and better workflows.',
        'intro': 'Advisory support complements training by helping clients apply what they learn in real operating environments.',
        'items': ['Process optimisation', 'Strategic and operational guidance', 'Workflow improvement', 'Project improvement', 'Action planning', 'Application support']
    },
    {
        'number': '03', 'name': 'Insights & Performance Support', 'short': 'Measure progress, identify trends and keep improvement visible.',
        'intro': 'Performance support helps organisations track KPIs and project outcomes while creating feedback loops for continued improvement.',
        'items': ['Performance dashboards', 'KPI tracking', 'Project outcome monitoring', 'Trend identification', 'Actionable insights', 'Feedback loops']
    },
    {
        'number': '04', 'name': 'Research, Workshops & Awareness', 'short': 'Stay informed, build awareness and strengthen a culture of performance.',
        'intro': 'Additional programmes support research, practical workshops and awareness initiatives tailored to organisational needs.',
        'items': ['Research support', 'Awareness programmes', 'Focused workshops', 'Performance culture', 'Knowledge sharing', 'Pilot programmes']
    }
]

AUDIENCES = [
    ('SMEs', 'Growing businesses that need clarity and operational efficiency.', 'fa-building'),
    ('NGOs', 'Mission-driven organisations improving programme performance.', 'fa-hand-holding-heart'),
    ('Freelancers', 'Independent professionals building practical, confident skills.', 'fa-user-tie'),
    ('Teams & Institutions', 'Professional teams and projects that need confident decisions.', 'fa-people-group')
]

VALUES = [
    ('Integrity', 'Honest, transparent engagement.'),
    ('Practical Learning', 'Skills that apply on Monday morning.'),
    ('Accountability', 'Owning outcomes with clients.'),
    ('Continuous Improvement', 'Every cycle better than the last.'),
    ('Ethical Practice', 'Responsible, fair, compliant work.')
]

FAQS = [
    ('What makes RoundData different?', 'RoundData connects training, advisory and insights in one continuous system so knowledge is applied, measured and improved.'),
    ('Who can work with RoundData?', 'The profile is designed around SMEs, NGOs, freelancers, professional teams and institutions.'),
    ('Is training the main service?', 'Yes. Training and capacity building is the foundation, while advisory and insights support application and measurement.'),
    ('Can RoundData begin with a pilot?', 'Yes. The profile describes pilot programmes as an entry point for demonstrating value and measurable outcomes before larger commitments.'),
    ('Where does RoundData operate?', 'The company is based in Nairobi, Kenya, with a stated intention to expand its reach beyond Kenya as it grows.')
]

@app.context_processor
def inject_globals():
    return {'services': SERVICES, 'year': datetime.now().year}

@app.route('/')
def home():
    return render_template('index.html', audiences=AUDIENCES, values=VALUES, faqs=FAQS)

@app.route('/about')
def about():
    return render_template('about.html', values=VALUES)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        entry = {
            'timestamp': datetime.now().isoformat(timespec='seconds'),
            'name': request.form.get('name', '').strip(),
            'organisation': request.form.get('organisation', '').strip(),
            'email': request.form.get('email', '').strip(),
            'phone': request.form.get('phone', '').strip(),
            'interest': request.form.get('interest', '').strip(),
            'message': request.form.get('message', '').strip(),
        }
        if not entry['name'] or not entry['email'] or not entry['message']:
            flash('Please complete your name, email and message.', 'error')
            return render_template('contact.html')
        file = DATA_DIR / 'enquiries.csv'
        exists = file.exists()
        with file.open('a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=entry.keys())
            if not exists:
                writer.writeheader()
            writer.writerow(entry)
        flash('Thank you. Your enquiry has been received.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
