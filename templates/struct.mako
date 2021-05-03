% for s in structs:

template<typename Visitor>
void VisitStruct( ${ s.name }& obj, Visitor& visitor )
{
	% for v in s.fields:
	visitor("${ v[1] }", obj.${ v[1] });
	% endfor
}

template<typename Visitor>
void VisitStruct( ${ s.name }& obj, const Visitor& visitor )
{
        % for v in s.fields:
        visitor("${ v[1] }", obj.${ v[1] });
        % endfor
}

% endfor
