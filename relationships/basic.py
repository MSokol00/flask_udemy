from models import db, Puppy, Owner, Toy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# add puppies to db
db.session.add_all([rufus, fido])
db.session.commit()

# Check !
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

jose = Owner('Jose', rufus.id)

toy1 = Toy('Chew toy', rufus.id)
toy2 = Toy('Ball', rufus.id)
db.session.add_all([jose, toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())
