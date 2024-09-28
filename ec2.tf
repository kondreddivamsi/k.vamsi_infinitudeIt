resource "aws_instance" "web" {
  ami           = "ami-0ebfd941bbafe70c6"  # Replace with your desired AMI
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.main.id
  key_name      = "pem"          # Replace with your key pair

  tags = {
    Name = "MyWebServer"
  }
}

