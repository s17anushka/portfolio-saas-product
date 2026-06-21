from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(200), nullable=False)  # Comma-separated values
    github_link = db.Column(db.String(250))
    live_link = db.Column(db.String(250))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "tech_stack": [tech.strip() for tech in self.tech_stack.split(',')],
            "github_link": self.github_link,
            "live_link": self.live_link
        }