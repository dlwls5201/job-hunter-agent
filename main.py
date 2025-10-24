import dotenv

dotenv.load_dotenv()

from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class JobHunterCrew:

    @agent
    def job_search_agent(self):
        return Agent(
            config=self.agent_config['job_search_agent']
        )

    @agent
    def job_matching_agent(self):
        return Agent(
            config=self.agent_config['job_matching_agent']
        )

    @agent
    def resume_optimization_agent(self):
        return Agent(
            config=self.agent_config['resume_optimization_agent']
        )

    @agent
    def company_research_agent(self):
        return Agent(
            config=self.agent_config['company_research_agent']
        )

    @agent
    def interview_prep_agent(self):
        return Agent(
            config=self.agent_config['interview_prep_agent']
        )

    @task
    def job_extraction_task(self):
        return Task(
            config=self.task_config['job_extraction_task']
        )

    @task
    def job_matching_task(self):
        return Task(
            config=self.task_config['job_matching_task']
        )

    @task
    def job_selection_task(self):
        return Task(
            config=self.task_config['job_selection_task']
        )

    @task
    def resume_rewriting_task(self):
        return Task(
            config=self.task_config['resume_rewriting_task']
        )

    @task
    def company_research_task(self):
        return Task(
            config=self.task_config['company_research_task'],
            context=[
                self.job_selection_task(),
            ]
        )

    @task
    def interview_prep_task(self):
        return Task(
            config=self.task_config['interview_prep_task'],
            context=[
                self.job_selection_task(),
                self.resume_rewriting_task(),
                self.company_research_task(),
            ]
        )

    