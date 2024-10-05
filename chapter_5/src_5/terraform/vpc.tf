# Create Virtual Private Cloud.
resource "aws_vpc" "mwaa_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = var.tag
  }
}

# Create Internet Gateway.
resource "aws_internet_gateway" "mwaa_igw" {
  vpc_id = aws_vpc.mwaa_vpc.id
  tags = {
    Name = var.tag
  }
}

# Create Public Subnet 1.
resource "aws_subnet" "public_subnet_1" {
  vpc_id            = aws_vpc.mwaa_vpc.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "${var.region}a"
  tags = {
    Name = var.tag
  }
}

# Create Public Subnet 2.
resource "aws_subnet" "public_subnet_2" {
  vpc_id            = aws_vpc.mwaa_vpc.id
  cidr_block        = "10.0.4.0/24"
  availability_zone = "${var.region}b"
  tags = {
    Name = var.tag
  }
}

# Create Private Subnet 1.
resource "aws_subnet" "private_subnet_1" {
  vpc_id            = aws_vpc.mwaa_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "${var.region}a"
  tags = {
    Name = var.tag
  }
}

# Create Private Subnet 2.
resource "aws_subnet" "private_subnet_2" {
  vpc_id            = aws_vpc.mwaa_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "${var.region}b"
  tags = {
    Name = var.tag
  }
}

# Create Route Table for Public Subnets.
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.mwaa_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.mwaa_igw.id
  }
  tags = {
    Name = var.tag
  }
}

# Associate Public Subnet 1 with the Route Table.
resource "aws_route_table_association" "public_subnet_1_assoc" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_route_table.id
}

# Associate Public Subnet 2 with the Route Table.
resource "aws_route_table_association" "public_subnet_2_assoc" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_route_table.id
}

# Create Security Group for MWAA.
resource "aws_security_group" "mwaa_sg" {
  vpc_id = aws_vpc.mwaa_vpc.id
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.personal_public_ip]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = var.tag
  }
}