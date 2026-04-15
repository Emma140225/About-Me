using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Game
{
    internal class Warrior : Character
    {
        //Attributes
        public readonly string VERSION = "1.10";
        public override string Version => VERSION;
        
        //Constructor
        public Warrior(string name, int power, int vitality)
        {
            Name = name;
            Power = power;
            Vitality = vitality;
        }


        //Methods
        public override int Fight(int power)
        {
            Helper.PrintBox($"{Name} fights with {power} Power");
            int damage = (power * Vitality) / 1000;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.BackgroundColor = ConsoleColor.DarkGray;
            for (int hits = 0; hits < damage; hits++)
            {
                Console.Write("X--> ");
                Thread.Sleep(100);
            }
            Console.WriteLine();
            Console.ResetColor();

            return damage;
        }
    }
}
