import attr
import datacli


@attr.s(auto_attribs=True, frozen=True)
class Foo:
    a: int
    b: str



if __name__ == "__main__":
    print(datacli.clidata(Foo))
