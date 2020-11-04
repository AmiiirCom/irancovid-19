from covid import Covid
import json

covid = Covid(source="worldometers")
covid.get_data()

iran_casses = covid.get_status_by_country_name("iran")

confirmed = iran_casses['confirmed']
new_cases = iran_casses['new_cases']
deaths = iran_casses['deaths']
recovered = iran_casses['recovered']
active = iran_casses['active']
critical = iran_casses['critical']
new_deaths = iran_casses ['new_deaths']
total_tests = iran_casses['total_tests']
total_tests_per_million = int(iran_casses['total_tests_per_million'])
total_cases_per_million = int(iran_casses['total_cases_per_million'])
total_deaths_per_million = int(iran_casses['total_deaths_per_million'])
population = int(iran_casses['population'])

pr = json.dumps({
    'confirmed': confirmed,
    'new_cases': new_cases,
    'deaths': deaths,
    'recovered': recovered,
    'active': active,
    'critical': critical,
    'new_deaths': new_deaths,
    'total_tests': total_tests,
    'total_tests_per_million': total_tests_per_million,
    'total_cases_per_million': total_cases_per_million,
    'total_deaths_per_million': total_deaths_per_million,
    'population': population
})

print(pr)