using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Game
{
    internal class Helper
    {
        //Aufbau der Tabelle und Anordnung der Stats in die Zeilen
        public static void PrintStats(Character a, Character b)
        {
            Console.WriteLine();
            PrintCharacter("Name:", a, b);
            PrintCharacter("Version:", a, b);
            PrintCharacter("Power:", a, b);
            PrintCharacter("Vitality:", a, b);
        }

        //Übernimmt die Stats und setzt sie in die Tabelle ein
        private static void PrintCharacter(string label, Character a, Character b)
        {
            Console.WriteLine(
                label.PadRight(13) +
                GetValue(label, a).PadRight(12) +
                GetValue(label, b).PadRight(12));
        }

        //Label sucht die Variable mit dem entsprechenden Namen
        private static string GetValue(string label, Character c)
        {
            if (label == "Name:")
                return c.GetSetName;

            if (label == "Version:")
                return c.Version;

            if (label == "Power:")
                return c.StatsPower.ToString();

            if (label == "Vitality:")
                return c.StatsVitality.ToString();

            return "";
        }

        
        //MessageBox
        public static void PrintBox(params string[] lines)
        {
            int maxLenght = lines.Max(l => l.Length);
            int width = maxLenght + 5;

            Console.WriteLine("+" + new string('-', width - 2) + "+");

            foreach (var line in lines)
            {
                Console.WriteLine($"| {line.PadRight(maxLenght)}  |");
            }
            Console.WriteLine("+" + new string('-', width - 2) + "+");
        }
    }
}
