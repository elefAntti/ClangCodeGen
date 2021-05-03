#include <vector>

namespace Testing
{
	enum class Animals
	{
		Cat, //Test comments
		Dog,
		SomeBird
	};

	struct AStruct
	{
		int Version;
		int Type;
		int Length;
		float x;
		float y;
		std::vector<Animals> v;
	};
}