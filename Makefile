clean:
	# Remove the build
	sudo rm -rf build dist
	# And all of our pyc files
	find . -name '*.pyc' | xargs -n 100 rm
	# And lastly, .coverage files
	find . -name .coverage | xargs rm

nose:
	rm -f .coverage
	nosetests --exe --cover-package=lunchtime --with-coverage --cover-branches --logging-clear-handlers -v

test: nose
