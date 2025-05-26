"""Technology stack recommendation tool."""

import json
from langchain_core.tools import tool

@tool
def technology_stack_recommendations(architecture_type: str, scale: str) -> str:
    """Recommend technology stacks based on architecture and scale."""
    tech_stacks = {
        "microservices": {
            "backend": ["Node.js", "Python", "Java", "Go"],
            "database": ["PostgreSQL", "MongoDB", "Redis"],
            "messaging": ["Apache Kafka", "RabbitMQ", "AWS SQS"],
            "containerization": ["Docker", "Kubernetes"],
            "monitoring": ["Prometheus", "Grafana", "ELK Stack"]
        },
        "serverless": {
            "functions": ["AWS Lambda", "Google Cloud Functions", "Azure Functions"],
            "database": ["DynamoDB", "Firestore", "CosmosDB"],
            "api_gateway": ["AWS API Gateway", "Google Cloud Endpoints"],
            "monitoring": ["CloudWatch", "Datadog", "New Relic"]
        },
        "monolithic": {
            "backend": ["Django", "Spring Boot", "Ruby on Rails", "ASP.NET"],
            "database": ["PostgreSQL", "MySQL", "SQL Server"],
            "caching": ["Redis", "Memcached"],
            "monitoring": ["New Relic", "AppDynamics"]
        }
    }
    return json.dumps(tech_stacks.get(architecture_type, tech_stacks["monolithic"]))
