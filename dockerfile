FROM python:3.11
WORKDIR /structure_enquiry
COPY . .
CMD ["python", "student.py"]