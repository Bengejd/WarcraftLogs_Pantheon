from warcraftlogs.client import WarcraftLogsClient

API_CLIENT = '67ca98b0d5bf6fdfa37efdc43dfb5a97'
SERVER = 'Blaumeux'
GUILD = 'Pantheon'
SERVER_REGION = 'US'

def main():
    api_key = '67ca98b0d5bf6fdfa37efdc43dfb5a97'
    client = WarcraftLogsClient(api_key=api_key)

    zones = client.zones()
    reports = client.reports(server=SERVER, guild=GUILD, region=SERVER_REGION)
    parses = client.parses(server=SERVER, region=SERVER_REGION, name='Neekio')

    for p in parses:
        print(p.percentile, p.encounterName, p.reportID)


if __name__ == '__main__':
    main()