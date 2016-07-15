
string search;
ifstream inFile;

int main (){
    inFile.open(test.html);
    if(!inFile){
        cout << "Unable to open file" << endl;
        exit(1);
    }
    cout << "Enter word to search for: ";
    getline(cin,search);
    //search code goes here...
}
