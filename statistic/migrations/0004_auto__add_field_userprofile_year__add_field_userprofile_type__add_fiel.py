# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.year'
        db.add_column(u'statistic_userprofile', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default=1960),
                      keep_default=False)

        # Adding field 'UserProfile.type'
        db.add_column(u'statistic_userprofile', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'UserProfile.css'
        db.add_column(u'statistic_userprofile', 'css',
                      self.gf('django.db.models.fields.IntegerField')(default=80),
                      keep_default=False)

        # Adding field 'UserProfile.skf'
        db.add_column(u'statistic_userprofile', 'skf',
                      self.gf('django.db.models.fields.IntegerField')(default=120),
                      keep_default=False)

        # Adding field 'UserProfile.hslpvp'
        db.add_column(u'statistic_userprofile', 'hslpvp',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.hslpnp'
        db.add_column(u'statistic_userprofile', 'hslpnp',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.moch'
        db.add_column(u'statistic_userprofile', 'moch',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.kreat'
        db.add_column(u'statistic_userprofile', 'kreat',
                      self.gf('django.db.models.fields.IntegerField')(default=85),
                      keep_default=False)

        # Adding field 'UserProfile.bilirubin'
        db.add_column(u'statistic_userprofile', 'bilirubin',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.ast'
        db.add_column(u'statistic_userprofile', 'ast',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.alt'
        db.add_column(u'statistic_userprofile', 'alt',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.glukosa'
        db.add_column(u'statistic_userprofile', 'glukosa',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


        # Changing field 'UserProfile.dat'
        db.alter_column(u'statistic_userprofile', 'dat', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'UserProfile.sat'
        db.alter_column(u'statistic_userprofile', 'sat', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):
        # Deleting field 'UserProfile.year'
        db.delete_column(u'statistic_userprofile', 'year')

        # Deleting field 'UserProfile.type'
        db.delete_column(u'statistic_userprofile', 'type')

        # Deleting field 'UserProfile.css'
        db.delete_column(u'statistic_userprofile', 'css')

        # Deleting field 'UserProfile.skf'
        db.delete_column(u'statistic_userprofile', 'skf')

        # Deleting field 'UserProfile.hslpvp'
        db.delete_column(u'statistic_userprofile', 'hslpvp')

        # Deleting field 'UserProfile.hslpnp'
        db.delete_column(u'statistic_userprofile', 'hslpnp')

        # Deleting field 'UserProfile.moch'
        db.delete_column(u'statistic_userprofile', 'moch')

        # Deleting field 'UserProfile.kreat'
        db.delete_column(u'statistic_userprofile', 'kreat')

        # Deleting field 'UserProfile.bilirubin'
        db.delete_column(u'statistic_userprofile', 'bilirubin')

        # Deleting field 'UserProfile.ast'
        db.delete_column(u'statistic_userprofile', 'ast')

        # Deleting field 'UserProfile.alt'
        db.delete_column(u'statistic_userprofile', 'alt')

        # Deleting field 'UserProfile.glukosa'
        db.delete_column(u'statistic_userprofile', 'glukosa')


        # Changing field 'UserProfile.dat'
        db.alter_column(u'statistic_userprofile', 'dat', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'UserProfile.sat'
        db.alter_column(u'statistic_userprofile', 'sat', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'statistic.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'alt': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ast': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bilirubin': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'css': ('django.db.models.fields.IntegerField', [], {'default': '80'}),
            'dat': ('django.db.models.fields.IntegerField', [], {'default': '80'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'glukosa': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'hslpnp': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'hslpvp': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kreat': ('django.db.models.fields.IntegerField', [], {'default': '85'}),
            'moch': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sat': ('django.db.models.fields.IntegerField', [], {'default': '120'}),
            'skf': ('django.db.models.fields.IntegerField', [], {'default': '120'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1960'})
        }
    }

    complete_apps = ['statistic']