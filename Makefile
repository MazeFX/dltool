bold = \e[1m
normal = \e[0m

GREEN = \033[32m
CYAN = \033[1;36m
WHITE = \033[0m

PROJECT_FOLDER = src/dltool


.PHONY: test
test:
	@echo "$(CYAN)>---------------------< $(GREEN)$(bold)Running PyTest$(normal) $(CYAN)>---------------------<$(WHITE)"
	@pytest -r f --cov=$(PROJECT_FOLDER) --cov-fail-under=35 tests/

.PHONY: test-html
test-html:
	@echo "$(CYAN)>---------------------<$(GREEN)$(bold)Running Test-HTML$(normal)$(CYAN)>--------------------<$(WHITE)"
	@pytest -r f --cov=$(PROJECT_FOLDER) --cov-fail-under=35 --cov-report=html tests/

.PHONY: black
black:
	@echo "$(CYAN)>---------------------< $(GREEN)$(bold)Running Black$(normal)  $(CYAN)>---------------------<$(WHITE)"
	@black --extend-exclude ".*/notebooks.*" .

.PHONY: isort
isort:
	@echo "$(CYAN)>---------------------< $(GREEN)$(bold)Running Isort$(normal)  $(CYAN)>---------------------<$(WHITE)"
	@isort $(PROJECT_FOLDER) tests

.PHONY: docs
docs:
	@echo "$(CYAN)>---------------------< $(GREEN)$(bold)Update Docs$(normal)    $(CYAN)>---------------------<$(WHITE)"; \
	cd ./docs; make html

.PHONY: docs-coverage
docs-coverage:
	@echo "$(CYAN)>---------------------< $(GREEN)$(bold)Update Docs$(normal)    $(CYAN)>---------------------<$(WHITE)"; \
	cd ./docs; make coverage

.PHONY: pylint  ## Lint using pylint.
pylint:
	@echo "$(CYAN)>---------------------< $(GREEN)$(bold)Running PyLint$(normal) $(CYAN)>---------------------<$(WHITE)"
	@pylint --fail-under=7.5 $(PROJECT_FOLDER)

ci: | black isort pylint test ## Run CI steps locally.
