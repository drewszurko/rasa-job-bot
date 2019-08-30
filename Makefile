help:
	@echo "    train-nlu"
	@echo "        Train Rasa NLU model."
	@echo "    train-core"
	@echo "        Train Rasa Core model."
	@echo "    run-core"
	@echo "        Start command line core server."
	@echo "    run-action-server"
	@echo "        Start action server."
	@echo "    run"
	@echo "        Start both core and action server."

train-nlu:
	python -m rasa_nlu.train -c config/nlu_config.yml --fixed_model_name current --data data/nlu.md --project nlu -o models --verbose

train-core:
	python -m rasa_core.train -c config/core_config.yml -d domain.yml -s data/stories.md -o models/dialogue

run-core:
	python -m rasa_core.run --nlu models/nlu/current --core models/dialogue --endpoints endpoints.yml --verbose

run-action-server:
	python -m rasa_core_sdk.endpoint --actions actions

run:
	make run-action-server&
	make run-core
