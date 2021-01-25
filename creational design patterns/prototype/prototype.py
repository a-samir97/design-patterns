import copy

class Website:

    def __init__(self, name, domain, description, author, **kwargs):

        self.name = name
        self.domain = domain
        self.description = description
        self.author = author

        for key in kwargs:
            setattr(self, key, kwargs[key])
    
    def __str__(self):
        return self.name + " | " + self.domain + " | " + self.author


class Prototype:

    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier, obj):
        del self.objects[identifier]
    
    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier) 
        if not found: 
            raise ValueError(f'Incorrect object identifier:{identifier}') 
    
        obj = copy.deepcopy(found) 
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj

def main(): 
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website('ContentGardening', 
            domain='contentgardening.com',
            description='Automation and data-driven apps', 
            author='Kamon Ayeva',
            category='Blog',
            keywords=keywords)

    prototype = Prototype() 
    identifier = 'ka-cg-1' 
    prototype.register(identifier, site1)

    site2 = prototype.clone(identifier, 
            name='ContentGardeningPlayground',
            domain='play.contentgardening.com', 
            description='Experimentation for techniques featured on the blog', 
            category='Membership site',
            creation_date='2018-08-01')    

    print(site1)
    print(site2)

if __name__=='__main__':
    main()