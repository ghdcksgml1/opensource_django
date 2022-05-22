from django.db import models


# class ProblemList(models.Model):
#     id = models.AutoField(primary_key=True)
#     problemList_name = models.CharField(max_length=100)


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    # problemList_id = models.ForeignKey(ProblemList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)
    question4 = models.CharField(max_length=100)
    answer_number = models.IntegerField(default=0)
    success = models.IntegerField(default=0)
    fail = models.IntegerField(default=0)

