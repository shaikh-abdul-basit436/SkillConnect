from app import app
from models.user import db
from models.skill import Skill

skills = {

    "Programming Languages":[
        "C",
        "C++",
        "Java",
        "Python",
        "JavaScript",
        "TypeScript",
        "C#",
        "Go",
        "Rust",
        "Kotlin",
        "Swift",
        "PHP",
        "Ruby",
        "R",
        "MATLAB",
        "Scala",
        "Dart",
        "Perl",
        "Shell Scripting",
        "SQL",
        "HTML",
        "CSS"
    ],

    "Web Development":[
        "Bootstrap",
        "Tailwind CSS",
        "React",
        "Angular",
        "Vue",
        "Node.js",
        "Express.js",
        "Next.js",
        "Flask",
        "Django",
        "Laravel",
        "REST API",
        "GraphQL"
    ],

    "Mobile Development":[
        "Android",
        "Flutter",
        "React Native",
        "Firebase",
        "Swift"
    ],

    "Database":[
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Oracle",
        "SQLite",
        "Redis",
        "Firebase Database"
    ],

    "Artificial Intelligence":[
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Computer Vision",
        "TensorFlow",
        "PyTorch",
        "OpenCV",
        "NumPy",
        "Pandas",
        "Scikit-learn"
    ],

    "Cloud & DevOps":[
        "AWS",
        "Azure",
        "Google Cloud",
        "Docker",
        "Kubernetes",
        "Jenkins",
        "Linux",
        "Git",
        "GitHub",
        "GitLab",
        "CI/CD"
    ],

    "Cyber Security":[
        "Ethical Hacking",
        "Network Security",
        "Cryptography",
        "Penetration Testing",
        "OWASP",
        "Digital Forensics",
        "Kali Linux"
    ],

    "Networking":[
        "Computer Networks",
        "TCP/IP",
        "DNS",
        "HTTP",
        "HTTPS",
        "VPN",
        "Cisco"
    ],

    "Software Engineering":[
        "OOP",
        "Data Structures",
        "Algorithms",
        "Operating Systems",
        "SDLC",
        "Agile",
        "Scrum",
        "Software Testing",
        "Debugging"
    ],

    "Electronics & IoT":[
        "Arduino",
        "Raspberry Pi",
        "Embedded Systems",
        "IoT",
        "Robotics",
        "PCB Design",
        "VLSI",
        "Microcontrollers"
    ],

    "Design":[
        "UI/UX",
        "Figma",
        "Canva",
        "Adobe Photoshop",
        "Adobe XD",
        "Wireframing",
        "Prototyping"
    ],

    "Communication":[
        "English Speaking",
        "Public Speaking",
        "Group Discussion",
        "Business Communication",
        "Technical Writing",
        "Email Writing"
    ],

    "Soft Skills":[
        "Leadership",
        "Teamwork",
        "Problem Solving",
        "Critical Thinking",
        "Time Management",
        "Creativity",
        "Adaptability"
    ],

    "Professional Skills":[
        "Resume Building",
        "Interview Preparation",
        "Coding Interview",
        "LinkedIn",
        "Portfolio Development"
    ],

    "Project Management":[
        "Kanban",
        "Project Planning",
        "Documentation",
        "Requirement Analysis",
        "Risk Management"
    ],

    "Office Tools":[
        "MS Word",
        "MS Excel",
        "MS PowerPoint",
        "Google Docs",
        "Google Sheets",
        "Notion",
        "Trello"
    ],

    "Business":[
        "Entrepreneurship",
        "Design Thinking",
        "Business Analytics",
        "Digital Marketing",
        "Financial Literacy"
    ]

}

with app.app_context():

    db.create_all()

    total = 0

    for category, values in skills.items():

        for name in values:

            exists = Skill.query.filter_by(
                skill_name=name
            ).first()

            if not exists:

                db.session.add(

                    Skill(

                        category=category,

                        skill_name=name,

                        description=name,

                        icon="fa-code"

                    )

                )

                total += 1

    db.session.commit()

    print(f"{total} Skills Added Successfully")