class SemanticCube:
    def __init__(self):
        self.semanticCubeDefinition = {
            '*': {
                'float': {
                    'int': 'float',
                    'float': 'float'
                },
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            },
            '/': {
                'float': {
                    'int': 'float',
                    'float': 'float'
                },
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            },
            '-': {
                'float': {
                    'int': 'float',
                    'float': 'float'
                },
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            },
            '+': {
                'float': {
                    'int': 'float',
                    'float': 'float'
                },
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            },
            '<': {
                'float': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'int': {
                    'int': 'boolean',
                    'float': 'boolean'
                }
            },
            '<=': {
                'float': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'int': {
                    'int': 'boolean',
                    'float': 'boolean'
                }
            },
            '>': {
                'float': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'int': {
                    'int': 'boolean',
                    'float': 'boolean'
                }
            },
            '>=': {
                'float': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'int': {
                    'int': 'boolean',
                    'float': 'boolean'
                }
            },
            '!=': {
                'float': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'int': {
                    'int': 'boolean',
                    'float': 'boolean'
                }
            },
            '==': {
                'float': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'int': {
                    'int': 'boolean',
                    'float': 'boolean'
                },
                'boolean': {
                    'boolean': 'boolean',
                }
            },
        }

    def getResultType(self, rightType, leftType, operator):
        resultType = self.semanticCubeDefinition[operator][leftType][rightType]
        return resultType
