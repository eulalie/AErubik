//***********************************************************************
//
//                               Cubitos
//
//***********************************************************************
 
 
//=======================================================================
//                                   Libraries
// ======================================================================



// ======================================================================
//                                 Project Files
// ======================================================================
#include "Cubitos.h"



using namespace std;
//#######################################################################
//                                                                      #
//                          Class Cubitos                               #
//                                                                      #
//#######################################################################

// ======================================================================
//                         Definition of static attributes
// ======================================================================

// ======================================================================
//                                  Constructors
// ======================================================================
Cubitos::Cubitos(int* pos, string col)
{
  x = pos[0];
  y = pos[1];
  z = pos[2];
  colors = col;

  //cout << "Creation of Cubito: "<<colors<<"\n";
}

// ======================================================================
//                                  Destructor
// ======================================================================
Cubitos::~Cubitos(void)
{
  //cout << "Destruction of Cubito"<<" "<<this<<"\n";
}

// ======================================================================
//                                 Public Methods
// ======================================================================
void Cubitos::print_cubito(void)
{
  cout << "cubito ("<<x<<','<<y<<','<<z<<") ("<<colors<<')'<<endl;
}
// ======================================================================
//                                Protected Methods
// ======================================================================

// ======================================================================
//                               Non inline accessors
// ======================================================================
