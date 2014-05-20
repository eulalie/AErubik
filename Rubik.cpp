//***********************************************************************
//
//                               Rubik
//
//***********************************************************************


 
 
//=======================================================================
//                                   Libraries
// ======================================================================



// ======================================================================
//                                 Project Files
// ======================================================================
#include "Rubik.h"


using namespace std;
//#######################################################################
//                                                                      #
//                          Class Rubik                                 #
//                                                                      #
//#######################################################################

// ======================================================================
//                         Definition of static attributes
// ======================================================================

// ======================================================================
//                                  Constructors
// ======================================================================
Rubik::Rubik(void)
{
  int x,y,z;
  cubos = new vector<Cubitos*>;
  char face_color[6] = {'r','o','b','g','y','w'};
  for (x=-1;x<=1;x++)
    {
      for (y=-1;y<=1;y++)
        {
          for(z=-1;z<=1;z++)
            {
              string colors = "nnnnnn";

              if(x!=0) colors[int((x+1)*0.5)] = face_color[int((x+1)*0.5)];
              if(y!=0) colors[int((y+1)*0.5+2)] = face_color[int((y+1)*0.5+2)];
              if(z!=0) colors[int((z+1)*0.5+4)] = face_color[int((z+1)*0.5+4)];

              int pos[3] = {x,y,z};

              Cubitos* cubito = new Cubitos(pos,colors);
              cubos->push_back(cubito);
            }
        }
    }


  cout << "Creation of Rubik"<<endl;
}


// ======================================================================
//                                  Destructor
// ======================================================================
Rubik::~Rubik(void)
{
  int i;
  for (i=0;i<cubos->size();i++)
    {
      delete cubos->at(i);
    }
  delete cubos;
  cout << "Destruction of Rubik "<<this<<endl;
}


// ======================================================================
//                                 Public Methods
// ======================================================================
void Rubik::print_rubik(void)
{
  int i;
  for (i=0;i<cubos->size();i++)
    {
      cubos->at(i)->print_cubito();
    }
}

vector<Cubitos*>* Rubik::give_face(int f)
{
  vector<Cubitos*>* face = new vector<Cubitos*>; //delete ?

  int i;
  for(i=0;i<cubos->size();i++)
    {
      bool condition;
      
      int x = cubos->at(i)->get_x();
      int y = cubos->at(i)->get_y();
      int z = cubos->at(i)->get_z();
      switch(f)
        {
        case 0:
          condition = (x==-1);
          break;
        case 1:
          condition = (x==1);
          break;
        case 2:
          condition = (y==-1);
          break;
        case 3:
          condition = (y==1);
          break;
        case 4:
          condition = (z==-1);
          break;
        case 5:
          condition = (z==1);
          break;
        }
      
      if(condition) face->push_back(cubos->at(i));

    }
  return(face);
}


// ======================================================================
//                                Protected Methods
// ======================================================================

// ======================================================================
//                               Non inline accessors
// ======================================================================
