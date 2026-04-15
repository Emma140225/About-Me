using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Game
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Mini Game ===\n\n");

            //create objects
            
            Game game1 = new Game();
            
            
            Warrior atlas = new Warrior("Atlas", 100, 100); //Name, Power, Vitality
            Fairy evelyn = new Fairy("Evelyn", 80, 100);


            //Add Player to Game
            game1.AddPlayer(atlas);
            game1.AddPlayer(evelyn);


            //Show Stats for 2 Players
            Helper.PrintStats(game1.Player[0], game1.Player[1]);

            //Battle
            Console.Write("\nPress any Key to start the Battle. \r");
            Console.ReadKey();
            game1.Play();
            Console.ReadKey();
            
            
        }
    }
}
