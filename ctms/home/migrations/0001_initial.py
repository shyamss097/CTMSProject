# Generated by Django 4.1.3 on 2022-12-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerid', models.IntegerField(db_column='PlayerID', primary_key=True, serialize=False)),
                ('playername', models.CharField(blank=True, db_column='PlayerName', max_length=30, null=True)),
                ('noofmatches', models.IntegerField(blank=True, db_column='NoOfMatches', null=True)),
                ('teamid', models.IntegerField(blank=True, db_column='TeamID', null=True)),
                ('runsscored', models.IntegerField(blank=True, db_column='RunsScored', null=True)),
                ('noofsixes', models.IntegerField(blank=True, db_column='NoOfSixes', null=True)),
                ('strikerate', models.FloatField(blank=True, db_column='StrikeRate', null=True)),
                ('noofwickets', models.IntegerField(blank=True, db_column='NoOfWickets', null=True)),
                ('economy', models.FloatField(blank=True, db_column='Economy', null=True)),
                ('bestbowling', models.CharField(blank=True, db_column='BestBowling', max_length=6, null=True)),
                ('nooffours', models.IntegerField(blank=True, db_column='NoOfFours', null=True)),
            ],
            options={
                'db_table': 'player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamid', models.IntegerField(db_column='TeamID', primary_key=True, serialize=False)),
                ('teamname', models.CharField(blank=True, db_column='TeamName', max_length=40, null=True)),
                ('teamrank', models.IntegerField(blank=True, db_column='TeamRank', null=True)),
                ('noofdraws', models.IntegerField(blank=True, db_column='NoOfDraws', null=True)),
                ('noofwins', models.IntegerField(blank=True, db_column='NoOfWins', null=True)),
                ('nooflosses', models.IntegerField(blank=True, db_column='NoOfLosses', null=True)),
                ('points', models.IntegerField(blank=True, db_column='Points', null=True)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Umpire',
            fields=[
                ('umpireid', models.IntegerField(db_column='umpireID', primary_key=True, serialize=False)),
                ('umpirename', models.CharField(blank=True, db_column='UmpireName', max_length=30, null=True)),
                ('noofmatches', models.IntegerField(blank=True, db_column='NoOfMatches', null=True)),
            ],
            options={
                'db_table': 'umpire',
                'managed': False,
            },
        ),
    ]