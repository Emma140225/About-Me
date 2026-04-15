using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Game
{
    internal class Fairy : Character
    {
        //Attributes
        public readonly string VERSION = "1.11";
        public override string Version => VERSION;

        private bool textAufgerufen = false;        //Fightmessage shows only once

        //Constructor
        public Fairy(string name, int power, int vitality)
        {
            Name = name;
            Power = power;
            Vitality = vitality;
        }

        //Methods
        public override int Fight(int power)
        {
            if (textAufgerufen)
            {
                textAufgerufen = false;
            }
            else
            {
                Helper.PrintBox($"{Name} fights with {power} Power");
                textAufgerufen=true;
            }


            int damage = (power * Vitality) / 1000;
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.BackgroundColor = ConsoleColor.DarkGray;
            for (int hits = 0; hits < damage; hits++)
            {
                Console.Write("@--* ");
                Thread.Sleep(100);

            }

            Console.ResetColor();

            Console.WriteLine();
            return damage;
        }
    }
}
