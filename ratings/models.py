from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100) 
    desc = models.TextField()
    link = models.TextField()
    overall_score = models.DecimalField(max_digits = 10, decimal_places = 9)
    qual_of_doc = models.DecimalField(max_digits = 10, decimal_places = 9)
    efficacy = models.DecimalField(max_digits = 10, decimal_places = 9)
    usability = models.DecimalField(max_digits = 10, decimal_places = 9)
    free = models.BooleanField(default = False)
    online = models.BooleanField(default = False)
    review_count = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name
	
class ToolCat(models.Model):
    tool_id = models.ForeignKey('Tool')
    cat_id = models.ForeignKey('Category')

    def __str__(self):
        return str(self.tool_id) + " in " + str(self.cat_id)
	
class Rating(models.Model):
    tool_id = models.ForeignKey(Tool)
    comment = models.TextField()
    overall_rating = models.DecimalField(max_digits = 10, decimal_places = 9)
    qual_of_doc = models.DecimalField(max_digits = 10, decimal_places = 9)
    efficacy = models.DecimalField(max_digits = 10, decimal_places = 9)
    usability = models.DecimalField(max_digits = 10, decimal_places = 9)

    def __str__(self):
        return self.tool_id + ' ' + self.overall_rating
