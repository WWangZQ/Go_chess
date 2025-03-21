#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .logger import Logger
from .observable import Observable
from .observer import Observer, Subject, ObserverRegistry
from .singleton import Singleton, LazySingleton, ThreadSafeSingleton, SingletonRegistry
from .factory import Factory, SimpleFactory, FactoryMethod, AbstractFactory
from .mediator import Colleague, Mediator, ConcreteMediator, MediatorRegistry
from .memento import Memento, Originator, Caretaker, MementoRegistry
from .proxy import Subject, Proxy, VirtualProxy, ProtectionProxy, RemoteProxy, ProxyRegistry
from .template import TemplateMethod, TemplateRegistry
from .visitor import Element, Visitor, ObjectStructure, VisitorRegistry
from .iterator import Iterator, Aggregate, ListIterator, DictIterator, IteratorRegistry
from .state import State, StateContext, StateMachine
from .command import Command, CommandInvoker, CommandQueue, CommandRegistry
from .strategy import Strategy, StrategyContext, StrategyRegistry
from .chain import Handler, Chain, ChainRegistry
from .flyweight import Flyweight, FlyweightFactory, FlyweightRegistry
from .bridge import Implementor, Abstraction, BridgeRegistry
from .decorator import Component, Decorator, DecoratorRegistry
from .facade import Facade, FacadeRegistry
from .composite import Component, Leaf, Composite, CompositeRegistry
from .adapter import Target, Adaptee, Adapter, AdapterRegistry
from .prototype import Prototype, PrototypeRegistry, DeepCloneMixin, ShallowCloneMixin
from .builder import Product, Builder, Director, BuilderRegistry
from .abstract_factory import AbstractProductA, AbstractProductB, AbstractFactory, AbstractFactoryRegistry
from .factory_method import Product, Creator, FactoryMethodRegistry

__all__ = [
    'Logger',
    'Observable',
    'Observer',
    'Subject',
    'ObserverRegistry',
    'Singleton',
    'LazySingleton',
    'ThreadSafeSingleton',
    'SingletonRegistry',
    'Factory',
    'SimpleFactory',
    'FactoryMethod',
    'AbstractFactory',
    'Colleague',
    'Mediator',
    'ConcreteMediator',
    'MediatorRegistry',
    'Memento',
    'Originator',
    'Caretaker',
    'MementoRegistry',
    'Subject',
    'Proxy',
    'VirtualProxy',
    'ProtectionProxy',
    'RemoteProxy',
    'ProxyRegistry',
    'TemplateMethod',
    'TemplateRegistry',
    'Element',
    'Visitor',
    'ObjectStructure',
    'VisitorRegistry',
    'Iterator',
    'Aggregate',
    'ListIterator',
    'DictIterator',
    'IteratorRegistry',
    'State',
    'StateContext',
    'StateMachine',
    'Command',
    'CommandInvoker',
    'CommandQueue',
    'CommandRegistry',
    'Strategy',
    'StrategyContext',
    'StrategyRegistry',
    'Handler',
    'Chain',
    'ChainRegistry',
    'Flyweight',
    'FlyweightFactory',
    'FlyweightRegistry',
    'Implementor',
    'Abstraction',
    'BridgeRegistry',
    'Component',
    'Decorator',
    'DecoratorRegistry',
    'Facade',
    'FacadeRegistry',
    'Leaf',
    'Composite',
    'CompositeRegistry',
    'Target',
    'Adaptee',
    'Adapter',
    'AdapterRegistry',
    'Prototype',
    'PrototypeRegistry',
    'DeepCloneMixin',
    'ShallowCloneMixin',
    'Product',
    'Builder',
    'Director',
    'BuilderRegistry',
    'AbstractProductA',
    'AbstractProductB',
    'AbstractFactory',
    'AbstractFactoryRegistry',
    'Creator',
    'FactoryMethodRegistry'
] 