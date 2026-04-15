using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace Game
{
    internal class Game
    {
        public List<Character> Player = new List<Character>();

        //Add Player to List
        public void AddPlayer(Character player)
        {
            if (Player.Count < 2)
            {
                Player.Add(player);
                Console.WriteLine($"{player.GetSetName} as {player.GetType().Name} engaged!");
            }
            else
            {
                Console.WriteLine("To many players!");
            }
        }

        public void Play()
        {
            Random rnd = new Random();
            int counter = 1;
            int damageDealed1 = 0;
            int damageDealed2 = 0;

            while (Player[0].StatsVitality > 0 && Player[1].StatsVitality > 0)
            {
                Console.Clear();
                Console.WriteLine($"===Round {counter++} ===\n");

                //Show all Damaged dealt
                Helper.PrintBox(
                    $"{Player[0].GetSetName} dealed {damageDealed1} Damage in this Fight.",
                    $"{Player[1].GetSetName} dealed {damageDealed2} Damage in this Fight.");
                Console.WriteLine();
                
                
                //Random amount of Power for each Player, Range goes from 10 to Players max Power
                int power1 = rnd.Next(10, Player[0].StatsPower+1);
                int power2 = rnd.Next(10, Player[1].StatsPower+1);


                //Calculate and Show Fight from Player 0
                int damage1 = Player[0].Fight(power1);
                string output1 = $"{Player[0].GetSetName} deals {damage1} Damage to {Player[1].GetSetName}";
                Helper.PrintBox(output1);
                Console.WriteLine();
                damageDealed1 = damageDealed1 + damage1;


                //Calculate and Show Fight from Player 1
                int damage2 = Player[1].Fight(power2) + Player[1].Fight(power2 / rnd.Next(1, 3));
                string output2 = $"{Player[1].GetSetName} deals {damage2} Damage to {Player[0].GetSetName}";
                Helper.PrintBox(output2);
                damageDealed2 = damageDealed2 + damage2;


                //Delete Damage from Opponents Vitality
                Player[0].StatsVitality = Player[0].StatsVitality - damage2;
                Player[1].StatsVitality = Player[1].StatsVitality - damage1;


                Helper.PrintStats(Player[0], Player[1]);
                Thread.Sleep(1000);

            }
            Console.Clear();

            //Calculate Winner
            
            if (Player[0].StatsVitality < 1 && Player[1].StatsVitality < 1)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Helper.PrintBox($"Draw: {Player[0]} and {Player[1]} are Game over!");
            }
            else if (Player[0].StatsVitality < Player[1].StatsVitality)
            {
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Helper.PrintBox($"{Player[1].GetSetName} has won the Battle");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Helper.PrintBox($"{Player[0].GetSetName} has won the Battle");
            }
            Console.ResetColor();
        }

    }
}
