import flet as ft

def findMatches():
    matchesList = []
    matchesList = []
    match = {"id": 0, "homeTeam": "Manchester United", "awayTeam": "Aab", "homeOdds": 2, "drawOdds": 1.5, "awayOdds": 3}
    match1 = {"id": 1, "homeTeam": "Liverpool", "awayTeam": "Chelsea", "homeOdds": 2.5, "drawOdds": 2.0, "awayOdds": 3.5}
    match2 = {"id": 2, "homeTeam": "Arsenal", "awayTeam": "Tottenham", "homeOdds": 2.8, "drawOdds": 2.2, "awayOdds": 3.2}

    matchesList.extend([match, match1, match2])
    return matchesList

def main(page: ft.page):

    def appendOdds(event, id, bet, odds):
        print(id,bet,odds)

    def generateOddsFields(event):
        matches = findMatches()
        for match in matches:
            homeTeamLabel = ft.Text(value=f"{match.get("homeTeam")}   - ")
            awayTeamLabel = ft.Text(value=match.get("awayTeam"))
            homeOddsBtn = ft.ElevatedButton(text=match.get('homeOdds'), on_click=lambda e, m=match: appendOdds(e, m['id'], "1", m['homeOdds']))
            drawOddsBtn = ft.ElevatedButton(text=match.get('drawOdds'), on_click=lambda e, m=match: appendOdds(e, m['id'], "x", m['drawOdds']))
            awayOddsBtn = ft.ElevatedButton(text=match.get('awayOdds'), on_click=lambda e, m=match: appendOdds(e, m['id'], "2", m['awayOdds']))
            
            # Make them into a row
            matchRow = ft.Row(
                controls=[homeTeamLabel,awayTeamLabel,homeOddsBtn,drawOddsBtn,awayOddsBtn],
                spacing=10
            )
            # Insert the row into a container.
            matchContainer = ft.Container(
                content=matchRow,
                border=ft.border.all(1, "black"), 
                padding=10,  
                border_radius=5, 
                width=page.width * 0.7
            )
            page.add(matchContainer)

    
    clickBtn = ft.ElevatedButton(text="click", on_click=generateOddsFields)
    page.add(clickBtn)
    
ft.app(target=main)



