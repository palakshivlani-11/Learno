# Generated by Django 2.1.6 on 2019-03-22 20:50

import colorful.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct answer')),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('point_required', models.FloatField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='badge_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_entr', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LastStudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_entr', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300, null=True, verbose_name='Question')),
                ('point', models.IntegerField(default=0, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='quiz_logo/')),
                ('point', models.IntegerField(default=0, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('approved', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StageLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.IntegerField(choices=[(1, 'beginner'), (2, 'easy'), (3, 'normal'), (4, 'hard'), (5, 'very hard')], default=1)),
                ('color', colorful.fields.RGBColorField(default='#007bff')),
                ('required_exp', models.PositiveIntegerField(blank=True, db_index=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(blank=True, default='default-96.png', upload_to='picture_profile/')),
                ('exp', models.PositiveIntegerField(blank=True, db_index=True, default=1)),
                ('level', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.Question')),
                ('stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_stage', to='accounts.Stage')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage_answers', to='accounts.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(1, 'Novice'), (2, 'Apprentice'), (3, 'Trainee'), (4, 'Beginner'), (5, 'Amateur '), (6, 'Professional'), (7, 'Master'), (8, 'Wizard '), (9, 'Mage'), (10, 'White Mage'), (11, 'Regent'), (12, 'King')], default=1)),
                ('logo', models.ImageField(blank=True, default=None, upload_to='level_pic/')),
                ('description', models.TextField(max_length=200)),
                ('graduation_number', models.IntegerField(blank=True, null=True)),
                ('exp_required', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', colorful.fields.RGBColorField(default='#007bff')),
            ],
        ),
        migrations.CreateModel(
            name='TakenBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('score', models.FloatField()),
                ('badge', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='taken_badges', to='accounts.Badge')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_badges', to='accounts.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TakenQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_entr', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='accounts.Quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='accounts.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='interested_students', to='accounts.Tag'),
        ),
        migrations.AddField(
            model_name='student',
            name='quizzes',
            field=models.ManyToManyField(blank=True, related_name='quize_student', through='accounts.TakenQuiz', to='accounts.Quiz'),
        ),
        migrations.AddField(
            model_name='student',
            name='rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level', to='accounts.StudentLevel'),
        ),
        migrations.AddField(
            model_name='stage',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.StageLevel'),
        ),
        migrations.AddField(
            model_name='stage',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='accounts.Quiz'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='accounts.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questiones', to='accounts.Stage'),
        ),
        migrations.AddField(
            model_name='laststudentanswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.Question'),
        ),
        migrations.AddField(
            model_name='laststudentanswer',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_question_stage', to='accounts.Stage'),
        ),
        migrations.AddField(
            model_name='laststudentanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage_last_answers', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='completedstage',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stage_quizze', to='accounts.Quiz'),
        ),
        migrations.AddField(
            model_name='completedstage',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stages', to='accounts.Stage'),
        ),
        migrations.AddField(
            model_name='completedstage',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_stages', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='accounts.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'text')},
        ),
    ]
