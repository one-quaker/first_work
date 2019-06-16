RUN=python manage.py

run_gunicorn:
	gunicorn first_work.wsgi:application -w 2 -b :8000 --reload --log-level=debug --log-file=-

run_dev:
	$(RUN) runserver 0.0.0.0:8000

clean:
	rm -rfv *~*
	find . -name '*.pyc' -exec rm -fv {} \;

shell:
	$(RUN) shell_plus

makemigrations:
	$(RUN) makemigrations

showmigrations:
	$(RUN) showmigrations

migrate: clean
	$(RUN) migrate

collectstatic:
	$(RUN) collectstatic --noinput

create_admin:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | $(RUN) shell
