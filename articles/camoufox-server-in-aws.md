---
type: article_summary
title: 'THE LAB #90: Camoufox Server in AWS'
slug: camoufox-server-in-aws
canonical_url: https://www.scraping.club/p/camoufox-server-in-aws
publish_date: '2025-08-01'
visibility: premium
topics:
- scraping-infra
- anti-detect-browsers
- browser-automation
- proxies
description: How to deploy a Camoufox browser server on AWS with ECR, EC2 Auto Scaling and a Network Load Balancer, including why NLB fits better than ALB.
source_hash: db20704448af57fd
---

# THE LAB #90: Camoufox Server in AWS

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-08-01 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/camoufox-server-in-aws?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

After building a working Docker image for Camoufox, which took us several hours and generated plenty of questions on the TWSC Discord, the next problem is running it at scale. One container on one machine does not help much when you need a cluster of Camoufox instances behind your proxy infrastructure, with clients connecting over WebSocket to a remote browser server.

We took the image, already pushed to Amazon ECR, and deployed it on AWS. The setup uses EC2 instances in an Auto Scaling Group, each running one Camoufox container, with IAM roles and security groups controlling access. I explain the architecture with a diagram and go through the launch template and user data. Then I compare Application and Network Load Balancer for this kind of traffic and say which one we picked and why. The last part covers the Auto Scaling Group, with VPC and subnet placement. I also mention alternatives such as ECS and EKS.

## What's inside

- How the ECR, EC2, Auto Scaling Group, load balancer and IAM pieces fit together, with a Mermaid diagram of the flow from scraping client to container.
- What the EC2 launch template needs: AMI with Docker, instance role for reading from ECR, security group and a user data script that runs at every launch.
- ALB versus NLB for long-lived WebSocket connections, and what changes in listeners, target groups and health checks once you choose one.
- Why instances sit in private subnets and the NLB in public ones, and what outbound access the instances still need.

**In the full article:** The user data script as I ran it, the exact listener, target group and health check settings, the security group rules and the Auto Scaling Group configuration.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/camoufox-server-in-aws?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
