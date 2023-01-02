from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_like_answer_alter_like_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.answer')),
            ],
        ),
        migrations.CreateModel(
            name='LikeQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='likequestion',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
        migrations.AddField(
            model_name='likequestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_like', to='app.question'),
        ),
        migrations.AddField(
            model_name='likeanswer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_related3', to='app.profile'),
        ),
    ]