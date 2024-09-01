def rpsWinner(player1,player2):
    if (player1=='rock' and player2=='scissors') or (player1=='scissors'and player2=='paper') or (player1=='paper'and player2=='rock'):
        return 'player one'
    elif  (player2=='rock' and player1=='scissors') or (player2=='scissors'and player1=='paper') or (player2=='paper'and player1=='rock'):
        return 'player two'
    else:
        return 'tie'
    
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
