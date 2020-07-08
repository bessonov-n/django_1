from django.db import models

# Create your models here.
class ikntprofils(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)


class Mc3025(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)

class Mc3026(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)

class Mc4(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)

class A021(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)

class A022(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)

class A024(models.Model):
	name = models.TextField(db_index=True)
	val = models.TextField(db_index=True)

	def _str_(self):
		return '{}'.format(self.name)

class A302(models.Model):
	name = models.TextField()
	val = models.TextField()

	def _str_(self):
		return self.name


class A305(models.Model):
	name = models.TextField()
	val = models.TextField()

	def _str_(self):
		return self.name

class A402(models.Model):
	name = models.TextField()
	val = models.TextField()

	def _str_(self):
		return self.name

class A405(models.Model):
	name = models.TextField()
	val = models.TextField()

	def _str_(self):
		return self.name