from c4model import Model, Person, SoftwareSystem, Relationship

customer = Person(name='Personal Banking Customer',
                  description='A customer of the bank, with\n personal bank accounts.')

email = SoftwareSystem(name='E-mail System', description='The internal Microsoft Exchange e-mail system.',
                       is_external=True)
internet = SoftwareSystem(name='Internet Banking System',
                          description='Allows customers to view\n information about their bank\n accounts, and make payments.')
mainframe = SoftwareSystem(name='Mainframe Banking System',
                           description='Stores all of the core banking \n information about customers,\naccounts, transactions, etc.',
                           is_external=True)

c1 = (Model(name='c1', label='System Context diagram for Internet Banking System')
      .add_box(customer)
      .add_box(email)
      .add_box(mainframe)
      .add_box(internet)
      .add_relationship(
    Relationship(customer, internet, description='Views account\nbalances, and\nmakes payments\nusing'))
      .add_relationship(Relationship(internet, email, description='Sends e-mail\nusing'))
      .add_relationship(Relationship(email, customer, description='Sends e-mails to'))
      .add_relationship(
    Relationship(internet, mainframe, description='Gets account\n information from,\nand makes\npayments using'))
      .save()
      )
