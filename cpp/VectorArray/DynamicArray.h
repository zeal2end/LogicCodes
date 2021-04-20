
template <class T>
class DynamicArray{
	int CUR_MAX_SIZE;
	int CUR_SIZE;
	T **ARRAY;
		int nextHigherPowerOfTwo(int num){
			if(num == 0)return 0;
			int cur =1;
			while(cur<=num)cur<<=1;
			return cur;
		}
		void errorCheck(){
			if(CUR_MAX_SIZE >= 4e6){
				//cerr << "Array size is too large!! Probably get array Out of Bound \n";
			}
		}
	public:
		DynamicArray(int size = 0){
			CUR_SIZE = size;
			CUR_MAX_SIZE = nextHigherPowerOfTwo(size);
			errorCheck(); // checking probable errors;
			T now[CUR_MAX_SIZE];
			*ARRAY = now;
		}
		// tell the current capacity
		int capacity(){return CUR_MAX_SIZE;}

		bool is_empty(){return CUR_SIZE==0;}

		T at(int index){
			return *ARRAY[index];
			//cerr << "Array out of bound";
		}

		void push(T item){
			if(CUR_SIZE < CUR_MAX_SIZE)*ARRAY[CUR_SIZE++] = item;
			else{
				// dynamic size array
				CUR_MAX_SIZE <<=1;
				errorCheck();
				T NOW[CUR_MAX_SIZE]; // new big array

				for(int i = 0;i<CUR_SIZE;i++){
					NOW[i] = *ARRAY[i];
				}
				NOW[CUR_SIZE++] = item;
				*ARRAY = NOW;
			}
		}

		void insert(int index,T item){
			if(index < CUR_SIZE){
				*ARRAY[index] = item;
			}
			//cerr << "OUT OF BOUND"<<endl;
		}

		T pop(){
			if(CUR_SIZE <0)
				//cerr << "array out of bound " <<endl;
			return *ARRAY[--CUR_SIZE];
		}
		
		void Delete(int index){
			for(int i = index;i<CUR_SIZE-1;i++){
				swap(*ARRAY[i],*ARRAY[i+1]);
			}
			//cerr << "Item deleted "<< *ARRAY[CUR_SIZE-1] <<endl;
			CUR_SIZE--;
		}

};
