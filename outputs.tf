output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_id" {
  value = aws_subnet.main.id
}

output "ec2_instance_id" {
  value = aws_instance.web.id
}

output "api_endpoint" {
  value = aws_api_gateway_rest_api.my_api.execution_arn
}
