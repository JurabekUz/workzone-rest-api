
# MODEL: Company
EmploymentForm = [
    ('OF', 'In Office'),
    ('ON', 'Remote'),
    ('HY', 'Hybrid')
]

EmploymentType = [
    ('FT', 'Full-Time'),
    ('PT', 'Part-Time'),
    ('FR', 'Freelance'),
    ('CT', 'Contract'),
    ('IN', 'Internship'),
]

SalaryType = [
    ('HOUR', 'Hour'),
    ('DAY', 'Day'),
    ('MONTH', 'Month'),
    ('HM', 'Half-Month'),
    ('YEAR', 'Year')
]

Currency = [
    ('UZS', 'UZS'),
    ('RUB', 'RUB'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
]

# MODEL: Company

APPLY_STATUS  = (
    ('UR', 'Un-Read'),
    ('RD', 'Read'),
    ('', ''),
    ('CL', 'Canceled'),
)