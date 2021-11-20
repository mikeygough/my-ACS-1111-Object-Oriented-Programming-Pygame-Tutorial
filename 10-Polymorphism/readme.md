# Polymorphism

The game has many different objects. But it needs to manage them all at the same time. 

In the you've been working on this happens with Sprites. 

Remember! When class inherits from a super class it is the super class. In other words. If a `GameObject` in herits from `Sprite` then a `GameObject` is a `Sprite`. 

The same is true for `Apple`. The `Apple` inherits from `GameObject` and `GameObject` inherits from `Sprite`. 

Remember the inheritence chart: 

- `Sprite`
  - `GameObject`
    - `Apple`
    - `Strawberry`
    - `Bomb`

Since `Apple`, `Strawberry`, and `bomb` are all `GameObject`s we can use them in place of a `GameObject` when our program expects a `GameObject`. 

Where does that happen? Since `GameObject` can be rendered to the screen using the `render()` method. All of the subclasses inherit this method! 

