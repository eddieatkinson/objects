class Person(object):
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone
		self.friends = []
		self.greeting_count = 0
		self.greeted = []

	def __repr__(self):
		return "Name: %s, Email: %s, Phone: %s" % (self.name, self.email, self.phone)

	def greet(self, other_person):
		print "Hello, %s, I am %s!" % (other_person.name, self.name)
		self.greeting_count += 1
		self.greeted.append(other_person)

	def get_contact(self):
		print "%s's contact info:" % self.name
		print "Email: %s" % self.email
		print "Phone number: %s" % self.phone

	def add_friend(self, added_friend):
		self.friends.append(added_friend)

	def num_friend(self):
		print len(self.friends)

	def num_unique_people_greeted(self):
		self.unique_people = set(self.greeted)
		print len(self.unique_people)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
eddie = Person("Eddie", "eddie@eddie.com", "770-568-7008")
sonny.greet(jordan)
jordan.greet(sonny)
sonny.greet(jordan)
sonny.greet(sonny)
sonny.greet(eddie)
sonny.greet(eddie)
sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()