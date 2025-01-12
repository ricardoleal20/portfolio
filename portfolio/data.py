"""
Include data to add, using the models provided here.
We'll include data such as the work experience, the education and others.
"""
from portfolio.models import (
    WorkExperienceModel, ProjectModel,
    EducationalModel, EducationalType,
    OpenSourceModel, WorkVisaModel
)

# ========================================== #
#            WORK EXPERIENCE JOBS            #
# ========================================== #
WORK_EXPERIENCE: list[WorkExperienceModel] = [
    WorkExperienceModel(
        worked_date="September 2022 - Current",
        position_job="Sr. Software Engineer",
        company_and_city="Valiot, México",
        description_job="""
            As a member of the ValueChainOS product team, I'm responsible for backend development using Python. 
            My focus is on enhancing product automation by creating and maintaining essential tools such as our ORM 
            for interfacing with GraphQL and APIs for data sharing and connectivity using TypeScript and Elixir. 
            Additionally, I develop interfaces to address mathematical optimization problems, creating or updating 
            constraints for supported problems. I work on generalizing internal packages to streamline product 
            implementation and reduce workload and complexity, such as creating custom workers for running tasks 
            using multi-threading and reporting the current state of tasks to other interfaces within the company.
        """,
        software_skills=(
            "Python", "TypeScript", "GraphQL", "Software Architecture", "DevOps"
        ),
    ),
    WorkExperienceModel(
        worked_date="June 2021 - September 2022",
        position_job="Software Engineer",
        company_and_city="Valiot, México",
        description_job="""
            Developed mechanisms for monitoring and evaluating diverse data sets from both clients and our
            product, such as identifying cases where an invalid parameter is received or detecting client-reported
            errors stemming from product usage, in order to provide corrective recommendations. Designed and executed
            tailored functions for clients, focusing on data cleaning techniques and preprocessing approaches that
            include analyses and data evaluations. Designed unit tests for the implementations that maintain a test
            coverage of at least 90% for the implementation. Created tools using Python to address company challenges
            by establishing links between the backend, frontend, and client services, particularly to resolve issues
            like data transmission failures.
        """,
        software_skills=(
            "Python", "TypeScript", "GraphQL", "Software Architecture", "DevOps"
        ),
    ),
    WorkExperienceModel(
        worked_date="February 2020 - June 2021",
        position_job="Research Assistant",
        company_and_city="Facultad de Ciencias Físico Matemáticas, México",
        description_job="""
            Developed simulations of various materials to understand their behavior and analyze their reactions using 
            molecular dynamics techniques, programmed in Python and LAMMPS. Improved the results and execution time 
            of simulations using optimization techniques such as gradient methods. Utilized Python for the creation 
            and manipulation of nanostructures, as well as for data analysis and prediction of changes. Leveraged HPC 
            (High-Performance Computing) clusters to optimize the computational efficiency of simulations.
        """,
        software_skills=(
            "Python", "C++", "Java", "Data Science", "Applied Mathematics"
        ),
    )
]

# ========================================== #
#                 EDUCATION                  #
# ========================================== #
EDUCATION: list[EducationalModel] = [
    EducationalModel(
        education_type=EducationalType.UNIVERSITY,
        educational_entity="Universidad Internacional de la Rioja",
        study_subject="MSc Computational Science and Applied Mathematics",
        range_years="2023-Current (Part-Time, expected to end by early 2025.)",
        description="""
            Specialization in Computer Science, I work developing APIs for problem solutions in the 
            industry, using the adequate design pattern for the problem and using techniques to ensure 
            the correct CI/CD process of the projects.
            Deep knowledge in algorithms, data structures, numerical analysis, and software architecture.
            With this new expertise, I know how to optimize different processes in real life, not only my
            modeling using statistical or mathematical models, but also by
            applying the best solution for each kind of problem, using my software engineering
            skills to automate the process of this problem to have a unique "math problem" that
            can be used in different places by just implementing it. I understand better the
            applications of mathematics in real life, I know how to schedule daily tasks
            to improve the supply chain of industries and how to use the received data to model
            a digital twin of the problems that can be optimized. 
        """
    ),
    EducationalModel(
        education_type=EducationalType.UNIVERSITY,
        educational_entity="Universidad Autónoma de Nuevo León",
        study_subject="BSc Physics",
        range_years="2018-2021",
        description="""
            Specialization in Computational Physics, focusing on 
            Materials Science and Molecular Dynamics, developing 
            data analysis tools, fracture prediction in materials, 
            and optimization tools for the contours of different 
            atomic structures. During my bachelor's, I studied and learned
            not only how to apply mathematics to solve real problems,
            such as the entire physics world, but also to use it as a tool
            to model basically everything. Among this, I understand the
            benefits of using highly scalable tools (such as HPC) to model
            and simulate different kinds of problems or scenarios. I worked as a
            research assistant in the Materials Science department, using
            mathematical modeling to understand the materials' behavior in different
            situations.
        """
    )
]

# ========================================== #
#                 CERTIFICATES               #
# ========================================== #
CERTIFICATES: list[EducationalModel] = [
    EducationalModel(
        education_type=EducationalType.UNIVERSITY,
        educational_entity="Tecnologico Nacional de México",
        study_subject="Data Science Diploma",
        range_years="2024",
        url="https://drive.google.com/file/d/1y9uZ8FCk0c5SKR7FI-zjvFPAfVvAJcCR/view?usp=share_link",
        description="""
            This diploma validates my knowledge in the Data Science
            area. I know how to handle different data structures and large datasets, how to clean
            them efficiently, and how to deal with various problems that can arise in the industry,
            using statistical and machine learning models.
        """
    ),
    EducationalModel(
        education_type=EducationalType.CERTIFICATE,
        educational_entity="Scrum.org",
        study_subject="Professional Scrum Developer",
        range_years="2022",
        url="https://www.credly.com/badges/2cc0bbc8-dc92-4ff4-b69c-" +
        "0024f78c412b?source=linked_in_profile",
        description="""
            This certification validates my knowledge of Scrum. It has provided me with
            an understanding of Agile methodologies, how to manage project timelines,
            handle bugs, and address unexpected tasks, among other skills.
        """
    ),
    EducationalModel(
        education_type=EducationalType.CERTIFICATE,
        educational_entity="IBM",
        study_subject="Data Analysis with Python",
        range_years="2021",
        url="https://www.credly.com/badges/acaeda41-d221-4642-be9a-2181eb683fcb/public_url",
        description="""
            This certification validates my knowledge in data
            analysis. I know how to handle different data structures, clean data, and solve
            problems using data analysis tools.
        """
    ),
    EducationalModel(
        education_type=EducationalType.CERTIFICATE,
        educational_entity="AWS",
        study_subject="AWS Academy Cloud Foundations",
        range_years="2020",
        url="https://www.credly.com/badges/10aea289-b676-4ee3-8c2e-c47da07faadb",
        description="""
            This certification validates my knowledge in cloud
            computing. I know how to handle various AWS services
            and solve problems using cloud services.
        """
    ),
]

# ========================================== #
#                 PROJECTS                   #
# ========================================== #
PROJECTS: list[ProjectModel] = [
    ProjectModel(
        project_title="Adaptative GraphQL API",
        project_image="/projects/graphql.jpeg",
        url_github=None,
        url_project="https://graphql-demo.ricardoleal20.dev",
        description="""
            This project is a demo of an adaptive GraphQL API that can be used to
            query different endpoints and get the data that you need. This API is
            designed to be flexible and scalable, allowing you to query the data
            that you need, and nothing more. It is designed to be fast and efficient,
            also to be reusable in different projects.
        """,
        software_skills=(
            "Python", "GraphQL", "API Development",
            "FastAPI", "Dynamic Programming"
        )
    ),
    ProjectModel(
        project_title="Prediction based on random DNI",
        project_image="",
        url_github="https://github.com/ricardoleal20/dni-based-prediction",
        description="""This project implements and compares three different regression and
        classification methods: multiple linear regression, multiple linear regression with step-wise selection,
        elastic net regression, random forest and GBM. The objective is to generate a dataset based on a
        provided National Identity Document (DNI), train regression models, and evaluate their performance.
        """,
        software_skills=(
            "Python", "Data Science"
        )
    ),
    ProjectModel(
        project_title="SuperMarket Optimization schedule",
        project_image="",
        url_github="https://github.com/ricardoleal20/supermarket_problem",
        url_project="http://supermarket-opt.ricardoleal20.dev/",
        description="""
        This project implements a supermarket optimization schedule using a linear algorithm solver.
        The objective is to generate a schedule for the supermarket employees based on the number of
        employees available, the number of clients, and the time that each employee takes to attend each client.
        """,
        software_skills=(
            "Python", "Rust", "Applied Mathematics", "API Development"
        )
    )
]

# ========================================== #
#              OPEN SOURCE CODE              #
# ========================================== #
OPEN_SOURCE: list[OpenSourceModel] = [
    OpenSourceModel(
        project_title="PyMath Compute",
        project_image="/projects/pymath_compute.png",
        url_github="https://github.com/ricardoleal20/pymath_compute",
        url_project="https://pymath.ricardoleal20.dev",
        description="""PyMathCompute is a Python tool designed to handle
        mathematical variables, create and evaluate mathematical expressions,
        and perform various mathematical optimizations. This library is ideal 
        for modelling problems related to applied mathematics, optimization, 
        and related fields.
        """,
        software_skills=(
            "Python", "Rust", "API Development",
            "Software Architecture", "Applied Mathematics"
        )
    ),
    OpenSourceModel(
        project_title="SemPyVer",
        project_image="",
        url_github="https://github.com/ricardoleal20/sempyver",
        url_project="",
        description="""Tool for teams that manage the creation and modification
        of the CHANGELOG based on a specified set of changes. It allow to keep a clean
        right path for groups implementation.
        """,
        software_skills=(
            "Rust", "API Development"
        )
    )
]

# ========================================== #
#              WORK VISA MODELS              #
# ========================================== #
WORK_VISA: list[WorkVisaModel] = [
    # * Mexico Work Visas
    WorkVisaModel(
        visa_name="Citizenship",
        country="Mexico",
        description=(
            "As a citizen, I do not need any kind of visa to work in Mexico."
        ),
        eligibility_conditions=(
            "Requires to be a Mexican citizen."
        ),
        duration="N/A",
        application_fee=9999,
        processing_time="2-3 months",
        required_documents=[
            "Valid passport or ID",
        ],
        application_link=""
    ),
    # * USA Work Visas
    # WorkVisaModel(
    #     visa_name="H-1B Visa",
    #     country="United States",
    #     description="A visa for specialized professionals in fields" +
    #     " like IT, finance, and engineering.",
    #     eligibility_conditions="Requires a bachelor's degree or equivalent" +
    #     " and a job offer from a U.S. employer. Also, the employer must" +
    #     " sponsor the visa.",
    #     duration="3 years (extendable up to 6 years)",
    #     application_fee=460.00,
    #     processing_time="3-6 months",
    #     required_documents=[
    #         "Passport",
    #         "Degree certificates",
    #         "USA Job offer letter",
    #         "A sponsor employer",
    #         # "Proof of work experience"
    #     ],
    #     application_link="https://www.uscis.gov/h-1b"
    # ),
    WorkVisaModel(
        visa_name="TN Visa (Trade NAFTA)",
        country="United States",
        description=(
            "A non-immigrant visa for citizens of Mexico and Canada, "
            "allowing temporary employment in the United States in qualified professional roles." +
            " This, different from the H-1B visa, does not require a sponsor employer."
        ),
        eligibility_conditions=(
            "Applicants must be citizens of Mexico or Canada" +
            " and have a job offer in a NAFTA-listed "
            "occupation (e.g., accountants, engineers, scientists)." +
            " Proof of qualifications required."
        ),
        duration="3 years (renewable indefinitely under certain conditions)",
        application_fee=160.00,  # General consular processing fee
        processing_time="Varies by consulate or port of entry; typically 1-3 weeks",
        required_documents=[
            "Passport",
            "Degree certificates",
            "USA Job offer letter",
            "DS-160 application form"
        ],
        application_link="https://travel.state.gov/content/travel/en/us-visas/employment/tn.html"
    ),
    # * Canada Work Visas
    WorkVisaModel(
        visa_name="Working Holiday Visa (IEC)",
        country="Canada",
        description=(
            "A visa that allows Mexican citizens to travel and work temporarily in Canada "
            "without the need for a job offer or sponsor."
        ),
        eligibility_conditions=(
            "Applicants must be Mexican citizens aged 18-35, have a valid"
            " passport, and sufficient funds "
            "to support themselves upon arrival (minimum CAD 2,500)."
            " No job offer is required."
        ),
        duration="Up to 1 year",
        application_fee=156.00,  # Approximate fee in CAD
        processing_time="6-8 weeks",
        required_documents=[
            "Valid Mexican passport",
            "Proof of funds",
            "Police clearance certificate",
            "Application IRCC"
        ],
        application_link=(
            "https://www.canada.ca/en/immigration-refugees-citizenship/"
            "services/work-canada/iec.html"
        )
    )
]
