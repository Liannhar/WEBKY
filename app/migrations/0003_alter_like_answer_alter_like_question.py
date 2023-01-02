from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_answer_like_remove_like_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_related', to='app.answer'),
        ),
        migrations.AlterField(
            model_name='like',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_related1', to='app.question'),
        ),
    ]