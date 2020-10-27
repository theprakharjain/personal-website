from app import db
from app import BlogPost

all_data = BlogPost.query.filter_by(title=BlogPost.title).all()

print(all_data)
for data in all_data:
    print(data)
    db.session.delete(data)
    db.session.commit()
