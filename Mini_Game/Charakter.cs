using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Game
{
    internal abstract class Character
    {
        //Attributes
        protected string Name;
        protected int Power;
        protected int Vitality;
        public virtual string Version => "";




        //Properties
        public int StatsPower
        {
            get { return Power; }
            set { Power = value; }
        }
        public int StatsVitality
        {
            get {  return Vitality; }
            set { Vitality = (value > 100) ? 100 : value; }
        }

        public string GetSetName
        {
            get { return Name; }
        }

        //Methods

        public abstract int Fight(int power);






        }
}
