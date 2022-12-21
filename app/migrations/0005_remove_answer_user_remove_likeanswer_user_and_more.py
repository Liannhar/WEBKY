from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_likeanswer_likequestion_alter_profile_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='likeanswer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.AddField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likeanswer',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(to='app.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='likeanswer',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.answer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='likequestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('h', 'hot'), ('n', 'normal')], max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
