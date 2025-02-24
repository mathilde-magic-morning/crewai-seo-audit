from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class SeoAuditCrew:
    """CrewAI pour l'analyse technique SEO avec Screaming Frog"""

    # Chargement des fichiers de configuration YAML
    agents_config = "agents.yaml"
    tasks_config = "tasks.yaml"

    @agent
    def seo_crawler(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_crawler"],
            verbose=True
        )

    @task
    def crawl_task(self) -> Task:
        return Task(
            config=self.tasks_config["crawl_site"]
        )

    @crew
    def crew(self) -> Crew:
        """Crée le Crew pour l'audit SEO technique"""
        return Crew(
            agents=self.agents,  # Collecte automatique des agents
            tasks=self.tasks,  # Collecte automatique des tâches
            process=Process.sequential,
            verbose=True
        )
